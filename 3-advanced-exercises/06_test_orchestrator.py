"""
Exercise 6: Test Orchestrator
Testing Focus: Distributed test execution, resource management

Task: Build a distributed test execution and orchestration system.
This exercise focuses on parallel test execution, resource management, and distributed coordination.
"""

import time
import threading
import concurrent.futures
import queue
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Union, Callable, Set
from collections import defaultdict, deque
import json

class NodeStatus(Enum):
    """Status of execution nodes."""
    IDLE = "idle"
    BUSY = "busy"
    OFFLINE = "offline"
    ERROR = "error"
    MAINTENANCE = "maintenance"

class JobStatus(Enum):
    """Status of test jobs."""
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"

class JobPriority(Enum):
    """Priority levels for test jobs."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    URGENT = 4

@dataclass
class TestJob:
    """Represents a test job to be executed."""
    id: str
    name: str
    test_function: Callable
    parameters: Dict[str, Any] = field(default_factory=dict)
    priority: JobPriority = JobPriority.NORMAL
    tags: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    timeout_seconds: int = 300
    retry_count: int = 0
    max_retries: int = 3
    required_resources: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    estimated_duration: int = 60  # seconds

@dataclass
class JobResult:
    """Result of test job execution."""
    job_id: str
    status: JobStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_seconds: float = 0.0
    return_value: Any = None
    error_message: Optional[str] = None
    traceback: Optional[str] = None
    node_id: Optional[str] = None
    resource_usage: Dict[str, Any] = field(default_factory=dict)
    artifacts: Dict[str, str] = field(default_factory=dict)

@dataclass
class ExecutionNode:
    """Represents an execution node in the cluster."""
    id: str
    name: str
    host: str
    port: int
    status: NodeStatus = NodeStatus.IDLE
    capabilities: Dict[str, Any] = field(default_factory=dict)
    current_jobs: List[str] = field(default_factory=list)
    max_concurrent_jobs: int = 4
    last_heartbeat: datetime = field(default_factory=datetime.now)
    resource_info: Dict[str, Any] = field(default_factory=dict)

class JobScheduler(ABC):
    """Abstract base class for job schedulers."""
    
    @abstractmethod
    def schedule_job(self, job: TestJob, available_nodes: List[ExecutionNode]) -> Optional[str]:
        """Schedule a job to an appropriate node."""
        pass
    
    @abstractmethod
    def get_scheduling_score(self, job: TestJob, node: ExecutionNode) -> float:
        """Calculate scheduling score for job-node pair."""
        pass

class FIFOScheduler(JobScheduler):
    """First-In-First-Out job scheduler."""
    
    def schedule_job(self, job: TestJob, available_nodes: List[ExecutionNode]) -> Optional[str]:
        """
        Schedule job using FIFO strategy.
        
        Args:
            job (TestJob): Job to schedule
            available_nodes (list): Available execution nodes
            
        Returns:
            str or None: Selected node ID or None if no suitable node
            
        TODO: Implement this method
        """
        pass
    
    def get_scheduling_score(self, job: TestJob, node: ExecutionNode) -> float:
        """
        Calculate scheduling score for FIFO strategy.
        
        Args:
            job (TestJob): Job to score
            node (ExecutionNode): Node to score
            
        Returns:
            float: Scheduling score
            
        TODO: Implement this method
        """
        pass

class LoadBalancingScheduler(JobScheduler):
    """Load-balancing job scheduler."""
    
    def schedule_job(self, job: TestJob, available_nodes: List[ExecutionNode]) -> Optional[str]:
        """
        Schedule job using load balancing strategy.
        
        Args:
            job (TestJob): Job to schedule
            available_nodes (list): Available execution nodes
            
        Returns:
            str or None: Selected node ID or None if no suitable node
            
        TODO: Implement this method
        """
        pass
    
    def get_scheduling_score(self, job: TestJob, node: ExecutionNode) -> float:
        """
        Calculate scheduling score for load balancing.
        
        Args:
            job (TestJob): Job to score
            node (ExecutionNode): Node to score
            
        Returns:
            float: Scheduling score (higher = better)
            
        TODO: Implement this method
        """
        pass

class ResourceAwareScheduler(JobScheduler):
    """Resource-aware job scheduler."""
    
    def __init__(self):
        """Initialize resource-aware scheduler."""
        self.resource_weights = {"cpu": 1.0, "memory": 1.0, "disk": 0.5}
    
    def schedule_job(self, job: TestJob, available_nodes: List[ExecutionNode]) -> Optional[str]:
        """
        Schedule job considering resource requirements.
        
        Args:
            job (TestJob): Job to schedule
            available_nodes (list): Available execution nodes
            
        Returns:
            str or None: Selected node ID or None if no suitable node
            
        TODO: Implement this method
        """
        pass
    
    def get_scheduling_score(self, job: TestJob, node: ExecutionNode) -> float:
        """
        Calculate resource-aware scheduling score.
        
        Args:
            job (TestJob): Job to score
            node (ExecutionNode): Node to score
            
        Returns:
            float: Scheduling score
            
        TODO: Implement this method
        """
        pass
    
    def check_resource_compatibility(self, job: TestJob, node: ExecutionNode) -> bool:
        """
        Check if node has sufficient resources for job.
        
        Args:
            job (TestJob): Job requiring resources
            node (ExecutionNode): Node to check
            
        Returns:
            bool: True if node can handle job
            
        TODO: Implement this method
        """
        pass

class JobQueue:
    """Thread-safe job queue with priority support."""
    
    def __init__(self, max_size: int = 1000):
        """
        Initialize job queue.
        
        Args:
            max_size (int): Maximum queue size
        """
        self.max_size = max_size
        self.jobs: List[TestJob] = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.dependency_graph: Dict[str, Set[str]] = {}
    
    def enqueue(self, job: TestJob) -> bool:
        """
        Add job to queue.
        
        Args:
            job (TestJob): Job to enqueue
            
        Returns:
            bool: True if successfully enqueued
            
        TODO: Implement this method
        """
        pass
    
    def dequeue(self, timeout: float = None) -> Optional[TestJob]:
        """
        Remove and return next available job.
        
        Args:
            timeout (float): Timeout in seconds
            
        Returns:
            TestJob or None: Next job or None if timeout
            
        TODO: Implement this method
        """
        pass
    
    def peek(self) -> Optional[TestJob]:
        """
        Get next job without removing it.
        
        Returns:
            TestJob or None: Next job or None if empty
            
        TODO: Implement this method
        """
        pass
    
    def get_ready_jobs(self, completed_jobs: Set[str]) -> List[TestJob]:
        """
        Get jobs that are ready to run (dependencies satisfied).
        
        Args:
            completed_jobs (set): Set of completed job IDs
            
        Returns:
            list: Jobs ready for execution
            
        TODO: Implement this method
        """
        pass
    
    def build_dependency_graph(self) -> None:
        """
        Build dependency graph from queued jobs.
        
        TODO: Implement this method
        """
        pass
    
    def size(self) -> int:
        """
        Get queue size.
        
        Returns:
            int: Number of jobs in queue
            
        TODO: Implement this method
        """
        pass

class NodeManager:
    """Manages execution nodes in the cluster."""
    
    def __init__(self):
        """Initialize node manager."""
        self.nodes: Dict[str, ExecutionNode] = {}
        self.node_lock = threading.Lock()
        self.heartbeat_interval = 30  # seconds
        self.heartbeat_timeout = 90   # seconds
        self.monitoring_thread: Optional[threading.Thread] = None
        self.is_monitoring = False
    
    def register_node(self, node: ExecutionNode) -> bool:
        """
        Register a new execution node.
        
        Args:
            node (ExecutionNode): Node to register
            
        Returns:
            bool: True if successfully registered
            
        TODO: Implement this method
        """
        pass
    
    def unregister_node(self, node_id: str) -> bool:
        """
        Unregister an execution node.
        
        Args:
            node_id (str): ID of node to unregister
            
        Returns:
            bool: True if successfully unregistered
            
        TODO: Implement this method
        """
        pass
    
    def get_available_nodes(self) -> List[ExecutionNode]:
        """
        Get list of available nodes.
        
        Returns:
            list: Available execution nodes
            
        TODO: Implement this method
        """
        pass
    
    def update_node_status(self, node_id: str, status: NodeStatus) -> bool:
        """
        Update node status.
        
        Args:
            node_id (str): Node ID
            status (NodeStatus): New status
            
        Returns:
            bool: True if successfully updated
            
        TODO: Implement this method
        """
        pass
    
    def record_heartbeat(self, node_id: str, resource_info: Dict[str, Any] = None) -> bool:
        """
        Record heartbeat from node.
        
        Args:
            node_id (str): Node ID
            resource_info (dict): Current resource information
            
        Returns:
            bool: True if heartbeat recorded
            
        TODO: Implement this method
        """
        pass
    
    def start_monitoring(self) -> None:
        """
        Start node monitoring.
        
        TODO: Implement this method
        """
        pass
    
    def stop_monitoring(self) -> None:
        """
        Stop node monitoring.
        
        TODO: Implement this method
        """
        pass
    
    def check_node_health(self) -> List[str]:
        """
        Check health of all nodes.
        
        Returns:
            list: List of unhealthy node IDs
            
        TODO: Implement this method
        """
        pass
    
    def get_cluster_statistics(self) -> Dict[str, Any]:
        """
        Get cluster-wide statistics.
        
        Returns:
            dict: Cluster statistics
            
        TODO: Implement this method
        """
        pass

class JobExecutor:
    """Executes jobs on local or remote nodes."""
    
    def __init__(self, node_id: str):
        """
        Initialize job executor.
        
        Args:
            node_id (str): ID of the node this executor runs on
        """
        self.node_id = node_id
        self.running_jobs: Dict[str, threading.Thread] = {}
        self.job_results: Dict[str, JobResult] = {}
        self.executor_lock = threading.Lock()
        self.max_concurrent_jobs = 4
    
    def execute_job(self, job: TestJob) -> JobResult:
        """
        Execute a test job.
        
        Args:
            job (TestJob): Job to execute
            
        Returns:
            JobResult: Execution result
            
        TODO: Implement this method
        """
        pass
    
    def execute_job_async(self, job: TestJob) -> str:
        """
        Execute job asynchronously.
        
        Args:
            job (TestJob): Job to execute
            
        Returns:
            str: Execution thread ID
            
        TODO: Implement this method
        """
        pass
    
    def cancel_job(self, job_id: str) -> bool:
        """
        Cancel a running job.
        
        Args:
            job_id (str): ID of job to cancel
            
        Returns:
            bool: True if successfully cancelled
            
        TODO: Implement this method
        """
        pass
    
    def get_job_status(self, job_id: str) -> Optional[JobStatus]:
        """
        Get status of a job.
        
        Args:
            job_id (str): Job ID
            
        Returns:
            JobStatus or None: Job status or None if not found
            
        TODO: Implement this method
        """
        pass
    
    def get_running_jobs(self) -> List[str]:
        """
        Get list of currently running job IDs.
        
        Returns:
            list: Running job IDs
            
        TODO: Implement this method
        """
        pass
    
    def cleanup_completed_jobs(self) -> int:
        """
        Clean up completed job results.
        
        Returns:
            int: Number of cleaned up jobs
            
        TODO: Implement this method
        """
        pass

class TestOrchestrator:
    """Main orchestrator for distributed test execution."""
    
    def __init__(self, scheduler: JobScheduler = None):
        """
        Initialize test orchestrator.
        
        Args:
            scheduler (JobScheduler): Job scheduler to use
        """
        self.scheduler = scheduler or LoadBalancingScheduler()
        self.job_queue = JobQueue()
        self.node_manager = NodeManager()
        self.executors: Dict[str, JobExecutor] = {}
        self.job_results: Dict[str, JobResult] = {}
        self.completed_jobs: Set[str] = set()
        self.orchestrator_thread: Optional[threading.Thread] = None
        self.is_running = False
        self.metrics: Dict[str, Any] = defaultdict(int)
    
    def submit_job(self, job: TestJob) -> bool:
        """
        Submit a job for execution.
        
        Args:
            job (TestJob): Job to submit
            
        Returns:
            bool: True if successfully submitted
            
        TODO: Implement this method
        """
        pass
    
    def submit_jobs(self, jobs: List[TestJob]) -> int:
        """
        Submit multiple jobs for execution.
        
        Args:
            jobs (list): Jobs to submit
            
        Returns:
            int: Number of successfully submitted jobs
            
        TODO: Implement this method
        """
        pass
    
    def start_orchestration(self) -> None:
        """
        Start the orchestration process.
        
        TODO: Implement this method
        """
        pass
    
    def stop_orchestration(self) -> None:
        """
        Stop the orchestration process.
        
        TODO: Implement this method
        """
        pass
    
    def orchestration_loop(self) -> None:
        """
        Main orchestration loop.
        
        TODO: Implement this method
        """
        pass
    
    def get_job_result(self, job_id: str, timeout: float = None) -> Optional[JobResult]:
        """
        Get result of a job.
        
        Args:
            job_id (str): Job ID
            timeout (float): Timeout in seconds
            
        Returns:
            JobResult or None: Job result or None if not found/timeout
            
        TODO: Implement this method
        """
        pass
    
    def cancel_job(self, job_id: str) -> bool:
        """
        Cancel a job.
        
        Args:
            job_id (str): Job ID to cancel
            
        Returns:
            bool: True if successfully cancelled
            
        TODO: Implement this method
        """
        pass
    
    def get_orchestrator_status(self) -> Dict[str, Any]:
        """
        Get orchestrator status and statistics.
        
        Returns:
            dict: Status information
            
        TODO: Implement this method
        """
        pass
    
    def generate_execution_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive execution report.
        
        Returns:
            dict: Execution report
            
        TODO: Implement this method
        """
        pass

class WorkflowManager:
    """Manages complex test workflows with dependencies."""
    
    def __init__(self, orchestrator: TestOrchestrator):
        """
        Initialize workflow manager.
        
        Args:
            orchestrator (TestOrchestrator): Test orchestrator instance
        """
        self.orchestrator = orchestrator
        self.workflows: Dict[str, Dict[str, Any]] = {}
        self.workflow_results: Dict[str, Dict[str, Any]] = {}
    
    def create_workflow(self, name: str, jobs: List[TestJob], 
                       dependencies: Dict[str, List[str]] = None) -> str:
        """
        Create a test workflow.
        
        Args:
            name (str): Workflow name
            jobs (list): Jobs in the workflow
            dependencies (dict): Job dependencies
            
        Returns:
            str: Workflow ID
            
        TODO: Implement this method
        """
        pass
    
    def execute_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """
        Execute a workflow.
        
        Args:
            workflow_id (str): Workflow ID
            
        Returns:
            dict: Workflow execution results
            
        TODO: Implement this method
        """
        pass
    
    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """
        Get workflow execution status.
        
        Args:
            workflow_id (str): Workflow ID
            
        Returns:
            dict: Workflow status
            
        TODO: Implement this method
        """
        pass
    
    def validate_workflow(self, jobs: List[TestJob], 
                         dependencies: Dict[str, List[str]]) -> List[str]:
        """
        Validate workflow for circular dependencies and other issues.
        
        Args:
            jobs (list): Jobs in workflow
            dependencies (dict): Job dependencies
            
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass

# Sample test functions for demonstration
def sample_test_function_1(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sample test function 1.
    
    Args:
        data (dict): Test data
        
    Returns:
        dict: Test result
        
    TODO: Implement this function
    """
    pass

def sample_test_function_2(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sample test function 2.
    
    Args:
        config (dict): Test configuration
        
    Returns:
        dict: Test result
        
    TODO: Implement this function
    """
    pass

def sample_slow_test(duration: int = 5) -> Dict[str, Any]:
    """
    Sample slow test function.
    
    Args:
        duration (int): Test duration in seconds
        
    Returns:
        dict: Test result
        
    TODO: Implement this function
    """
    pass

def create_sample_test_jobs() -> List[TestJob]:
    """
    Create sample test jobs for demonstration.
    
    Returns:
        list: List of sample test jobs
        
    TODO: Implement this function
    """
    pass

def create_sample_execution_nodes() -> List[ExecutionNode]:
    """
    Create sample execution nodes for demonstration.
    
    Returns:
        list: List of sample execution nodes
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Test Orchestrator Exercise ===\n")
    
    # Initialize components
    load_balancer = LoadBalancingScheduler()
    resource_scheduler = ResourceAwareScheduler()
    orchestrator = TestOrchestrator(load_balancer)
    workflow_manager = WorkflowManager(orchestrator)
    
    print("1. Test Orchestrator Initialization:")
    print(f"Orchestrator initialized with {type(orchestrator.scheduler).__name__}")
    print(f"Job queue ready: {orchestrator.job_queue is not None}")
    print(f"Node manager ready: {orchestrator.node_manager is not None}")
    print(f"Workflow manager ready: {workflow_manager is not None}")
    
    # Create and register execution nodes
    print("\n2. Execution Node Setup:")
    
    sample_nodes = create_sample_execution_nodes()
    print(f"Created {len(sample_nodes)} sample execution nodes")
    
    for node in sample_nodes:
        success = orchestrator.node_manager.register_node(node)
        print(f"  Registered node {node.name}: {success}")
        
        # Create executor for each node
        executor = JobExecutor(node.id)
        orchestrator.executors[node.id] = executor
    
    # Start node monitoring
    orchestrator.node_manager.start_monitoring()
    print("Node monitoring started")
    
    # Test job creation and submission
    print("\n3. Job Creation and Submission:")
    
    sample_jobs = create_sample_test_jobs()
    print(f"Created {len(sample_jobs)} sample test jobs")
    
    submitted_count = orchestrator.submit_jobs(sample_jobs)
    print(f"Successfully submitted {submitted_count} jobs")
    
    # Show job queue status
    queue_size = orchestrator.job_queue.size()
    print(f"Jobs in queue: {queue_size}")
    
    # Test different scheduling strategies
    print("\n4. Scheduling Strategy Tests:")
    
    available_nodes = orchestrator.node_manager.get_available_nodes()
    print(f"Available nodes: {len(available_nodes)}")
    
    if sample_jobs and available_nodes:
        test_job = sample_jobs[0]
        
        # Test FIFO scheduler
        fifo_scheduler = FIFOScheduler()
        selected_node = fifo_scheduler.schedule_job(test_job, available_nodes)
        print(f"  FIFO scheduler selected node: {selected_node}")
        
        # Test load balancing scheduler
        lb_node = load_balancer.schedule_job(test_job, available_nodes)
        print(f"  Load balancing scheduler selected node: {lb_node}")
        
        # Test resource-aware scheduler
        resource_node = resource_scheduler.schedule_job(test_job, available_nodes)
        print(f"  Resource-aware scheduler selected node: {resource_node}")
    
    # Test job execution
    print("\n5. Job Execution Tests:")
    
    # Start orchestration
    orchestrator.start_orchestration()
    print("Orchestration started")
    
    # Wait for some jobs to complete
    time.sleep(3)
    
    # Check job results
    completed_jobs = []
    for job in sample_jobs[:3]:  # Check first 3 jobs
        result = orchestrator.get_job_result(job.id, timeout=1.0)
        if result:
            completed_jobs.append(result)
            print(f"  Job {job.name}: {result.status.value} ({result.duration_seconds:.2f}s)")
    
    print(f"Completed jobs: {len(completed_jobs)}")
    
    # Test job cancellation
    print("\n6. Job Cancellation Tests:")
    
    if len(sample_jobs) > 3:
        cancel_job = sample_jobs[3]
        cancel_success = orchestrator.cancel_job(cancel_job.id)
        print(f"Job cancellation for {cancel_job.name}: {cancel_success}")
    
    # Test workflow management
    print("\n7. Workflow Management Tests:")
    
    # Create a simple workflow
    workflow_jobs = sample_jobs[:4] if len(sample_jobs) >= 4 else sample_jobs
    workflow_dependencies = {}
    
    if len(workflow_jobs) >= 2:
        # Create simple dependency: job2 depends on job1
        workflow_dependencies[workflow_jobs[1].id] = [workflow_jobs[0].id]
    
    if len(workflow_jobs) >= 4:
        # job4 depends on job2 and job3
        workflow_dependencies[workflow_jobs[3].id] = [workflow_jobs[1].id, workflow_jobs[2].id]
    
    workflow_id = workflow_manager.create_workflow(
        "Sample Workflow", 
        workflow_jobs, 
        workflow_dependencies
    )
    
    print(f"Created workflow: {workflow_id}")
    
    # Validate workflow
    validation_errors = workflow_manager.validate_workflow(workflow_jobs, workflow_dependencies)
    print(f"Workflow validation errors: {len(validation_errors)}")
    
    # Execute workflow
    workflow_results = workflow_manager.execute_workflow(workflow_id)
    print(f"Workflow execution initiated: {workflow_results.get('status', 'Unknown')}")
    
    # Test node health monitoring
    print("\n8. Node Health Monitoring:")
    
    # Record some heartbeats
    for node in sample_nodes:
        resource_info = {
            "cpu_usage": 25.5,
            "memory_usage": 60.2,
            "disk_usage": 40.0
        }
        heartbeat_recorded = orchestrator.node_manager.record_heartbeat(node.id, resource_info)
        print(f"  Heartbeat recorded for {node.name}: {heartbeat_recorded}")
    
    # Check node health
    unhealthy_nodes = orchestrator.node_manager.check_node_health()
    print(f"Unhealthy nodes: {len(unhealthy_nodes)}")
    
    # Get cluster statistics
    cluster_stats = orchestrator.node_manager.get_cluster_statistics()
    print(f"Cluster statistics: {cluster_stats}")
    
    # Test resource management
    print("\n9. Resource Management Tests:")
    
    if available_nodes and sample_jobs:
        test_job = sample_jobs[0]
        test_node = available_nodes[0]
        
        # Test resource compatibility
        is_compatible = resource_scheduler.check_resource_compatibility(test_job, test_node)
        print(f"Resource compatibility: {is_compatible}")
        
        # Test scheduling scores
        fifo_score = fifo_scheduler.get_scheduling_score(test_job, test_node)
        lb_score = load_balancer.get_scheduling_score(test_job, test_node)
        resource_score = resource_scheduler.get_scheduling_score(test_job, test_node)
        
        print(f"Scheduling scores:")
        print(f"  FIFO: {fifo_score:.2f}")
        print(f"  Load Balancing: {lb_score:.2f}")
        print(f"  Resource-Aware: {resource_score:.2f}")
    
    # Test job queue operations
    print("\n10. Job Queue Operations:")
    
    # Test dependency resolution
    orchestrator.job_queue.build_dependency_graph()
    ready_jobs = orchestrator.job_queue.get_ready_jobs(orchestrator.completed_jobs)
    print(f"Jobs ready for execution: {len(ready_jobs)}")
    
    # Test queue operations
    peek_job = orchestrator.job_queue.peek()
    if peek_job:
        print(f"Next job in queue: {peek_job.name}")
    
    # Test job executor operations
    print("\n11. Job Executor Tests:")
    
    if orchestrator.executors and sample_jobs:
        executor = list(orchestrator.executors.values())[0]
        test_job = sample_jobs[0]
        
        # Execute job synchronously
        sync_result = executor.execute_job(test_job)
        print(f"Synchronous execution: {sync_result.status.value}")
        
        # Execute job asynchronously
        if len(sample_jobs) > 1:
            async_job = sample_jobs[1]
            thread_id = executor.execute_job_async(async_job)
            print(f"Asynchronous execution started: {thread_id}")
            
            # Check job status
            time.sleep(0.5)
            job_status = executor.get_job_status(async_job.id)
            print(f"Async job status: {job_status.value if job_status else 'Unknown'}")
        
        # Get running jobs
        running_jobs = executor.get_running_jobs()
        print(f"Currently running jobs: {len(running_jobs)}")
        
        # Cleanup completed jobs
        cleaned_up = executor.cleanup_completed_jobs()
        print(f"Cleaned up {cleaned_up} completed jobs")
    
    # Test orchestrator status and reporting
    print("\n12. Status and Reporting:")
    
    # Get orchestrator status
    orchestrator_status = orchestrator.get_orchestrator_status()
    print(f"Orchestrator status: {orchestrator_status}")
    
    # Generate execution report
    execution_report = orchestrator.generate_execution_report()
    print(f"Execution report sections: {list(execution_report.keys())}")
    
    # Get workflow status
    workflow_status = workflow_manager.get_workflow_status(workflow_id)
    print(f"Workflow status: {workflow_status}")
    
    # Test performance metrics
    print("\n13. Performance Metrics:")
    
    # Wait a bit more for jobs to complete
    time.sleep(2)
    
    final_status = orchestrator.get_orchestrator_status()
    
    print(f"Final metrics:")
    print(f"  Total jobs submitted: {final_status.get('total_submitted', 0)}")
    print(f"  Jobs completed: {final_status.get('completed', 0)}")
    print(f"  Jobs failed: {final_status.get('failed', 0)}")
    print(f"  Jobs pending: {final_status.get('pending', 0)}")
    print(f"  Average execution time: {final_status.get('avg_execution_time', 0):.2f}s")
    
    # Test load balancing effectiveness
    node_load_distribution = {}
    for node in sample_nodes:
        node_load_distribution[node.name] = len(node.current_jobs)
    
    print(f"Node load distribution: {node_load_distribution}")
    
    # Test fault tolerance
    print("\n14. Fault Tolerance Tests:")
    
    # Simulate node failure
    if sample_nodes:
        failed_node = sample_nodes[0]
        orchestrator.node_manager.update_node_status(failed_node.id, NodeStatus.ERROR)
        print(f"Simulated failure of node: {failed_node.name}")
        
        # Check how orchestrator adapts
        available_after_failure = orchestrator.node_manager.get_available_nodes()
        print(f"Available nodes after failure: {len(available_after_failure)}")
        
        # Restore node
        orchestrator.node_manager.update_node_status(failed_node.id, NodeStatus.IDLE)
        print(f"Restored node: {failed_node.name}")
    
    # Test job retry mechanism
    print("\n15. Job Retry Mechanism:")
    
    # Create a job that will fail initially
    retry_job = TestJob(
        id=str(uuid.uuid4()),
        name="Retry Test Job",
        test_function=sample_test_function_1,
        parameters={"should_fail": True},
        max_retries=2
    )
    
    submitted = orchestrator.submit_job(retry_job)
    print(f"Submitted retry test job: {submitted}")
    
    # Wait and check result
    time.sleep(1)
    retry_result = orchestrator.get_job_result(retry_job.id, timeout=2.0)
    if retry_result:
        print(f"Retry job final status: {retry_result.status.value}")
        print(f"Retry attempts: {retry_job.retry_count}")
    
    # Cleanup and shutdown
    print("\n16. Cleanup and Shutdown:")
    
    # Stop orchestration
    orchestrator.stop_orchestration()
    print("Orchestration stopped")
    
    # Stop node monitoring
    orchestrator.node_manager.stop_monitoring()
    print("Node monitoring stopped")
    
    # Final statistics
    final_report = orchestrator.generate_execution_report()
    total_jobs = final_report.get('total_jobs', 0)
    successful_jobs = final_report.get('successful_jobs', 0)
    total_execution_time = final_report.get('total_execution_time', 0)
    
    print(f"\nFinal Execution Summary:")
    print(f"Total jobs: {total_jobs}")
    print(f"Successful jobs: {successful_jobs}")
    print(f"Success rate: {(successful_jobs/total_jobs*100) if total_jobs > 0 else 0:.1f}%")
    print(f"Total execution time: {total_execution_time:.2f}s")
    
    if total_jobs > 0:
        avg_time_per_job = total_execution_time / total_jobs
        print(f"Average time per job: {avg_time_per_job:.2f}s")
    
    print(f"\nTest Orchestrator Exercise Complete!")
    print(f"Registered nodes: {len(orchestrator.node_manager.nodes)}")
    print(f"Created workflows: {len(workflow_manager.workflows)}")
    print(f"Total job results: {len(orchestrator.job_results)}")
    
    print("\n" + "="*50)
    print("Test Orchestrator Exercise Complete!")
    print("="*50)